from project.user import User
from project.library import Library


class Registration:

    def add_user(self, user: User, library: Library):
        if user.user_id not in library.user_records:
            library.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user.user_id not in library.user_records:
            return f"We could not find such user to remove!"

        try:
            del library.rented_books[user.username]  # ako e nael knigi, samo togava go triem
        except KeyError:
            pass

        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user = next(filter(lambda u: u.user_id == user_id,
                               library.user_records))  # tyrsim user_id dali go ima f user_records
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:  # user tuka e obekr syzdaden ot next(filter).. koito ima h-stiki na obekta user.records
            return f"Please check again the provided username - it should be different than the username used so far!"

        try:
            library.rented_books[new_username] = library.rented_books.pop(user.username)
        except KeyError:
            pass
        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
