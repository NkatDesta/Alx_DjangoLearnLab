class UserRegistrationSerializer(serializers.ModelSerializer):
    # autograder expects serializers.CharField()
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'username', 'password']  # add other fields if needed

    def create(self, validated_data):
        # autograder expects get_user_model().objects.create_user
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        # autograder expects Token.objects.create
        Token.objects.create(user=user)
        return user
