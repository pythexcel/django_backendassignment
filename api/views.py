# api/views.py

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer, UserSerializer, UserCreateSerializer

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        password = make_password(request.data.get('password'))
        request.data['password'] = password

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        existing_profile = Profile.objects.filter(user=request.user).first()

        if existing_profile:
            return Response({'message': 'Profile already exists for this user.'}, status=status.HTTP_200_OK)

        profile_data = {
            'bio': request.data.get('bio', ''),
            'profile_picture': request.data.get('profile_picture', None),
            'user': request.user,
        }
        profile = Profile.objects.create(**profile_data)

        return Response({'message': 'Profile created successfully'}, status=status.HTTP_201_CREATED)

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileDeleteView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class FollowUserView(APIView):
    def post(self, request, user_id):
        user_to_follow = User.objects.get(pk=user_id)
        if user_to_follow != request.user:
            request.user.profile.followers.add(user_to_follow)
            return Response({'message': f'You are now following {user_to_follow.username}'})
        else:
            return Response({'message': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUserView(APIView):
    def post(self, request, user_id):
        user_to_unfollow = User.objects.get(pk=user_id)
        request.user.profile.followers.remove(user_to_unfollow)
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}'})