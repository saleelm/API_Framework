import random
import string


class TestDataGenerator:

    @staticmethod
    def _generate_random_string(length: int, allowed_chars: str = string.ascii_letters) -> str:
        """Generates a random string of a given length using the allowed characters."""
        return ''.join(random.choice(allowed_chars) for _ in range(length))

    @staticmethod
    def generate_random_body():
        """Generates a random API body based on the provided constraints."""

        id_str = str(random.randint(1000000000000, 9999999999999))
        name_length = random.randint(1, 50)
        name_str = TestDataGenerator._generate_random_string(name_length, allowed_chars=string.ascii_letters)
        phone_str = TestDataGenerator._generate_random_string(10, allowed_chars=string.digits)

        body = {
            "id": id_str,
            "name": name_str,
            "phone_number": phone_str
        }

        return body

    @staticmethod
    def generate_body_with_string_phone():
        """Generate body with phone_number as a string."""
        body = TestDataGenerator.generate_random_body()
        body['phone_number'] = TestDataGenerator._generate_random_string(10)
        return body

    @staticmethod
    def generate_body_with_max_values():
        """Generate body with max allowed values."""
        id_str = str(random.randint(1000000000000, 9999999999999))
        # Assuming maximum name length allowed is 255 and phone_number is 15
        max_name = "A" * 255
        max_phone_number = "9" * 15

        return {
            "id": id_str,
            "name": max_name,
            "phone_number": max_phone_number
        }

    @staticmethod
    def generate_body_with_non_english_name():
        """Generate body with non-English characters in name."""
        body = TestDataGenerator.generate_random_body()
        body['name'] = TestDataGenerator._generate_random_string(10, allowed_chars="Jöhn-äçčêñtś")
        return body
