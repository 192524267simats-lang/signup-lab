def signup(username, password):
    if not username:
        return "Username required"
    if len(password) < 6:
        return "Password must be at least 6 characters"
    return "Signup successful"


if __name__ == "__main__":
    print(signup("student", "123456"))
    print(signup("", "123456"))
    print(signup("student", "123"))
