from django import template
import string, random


register = template.Library()


@register.simple_tag
def get_random_password() -> str:
    """Generate a random password with 10 characters.
    Include uppercase letters, lowercase letters, digits, and special characters."""
    quantity = 10
    characters = string.ascii_letters + string.digits + string.punctuation + ''.join([str(_) for _ in range(10)])
    password = ''.join(random.choice(characters) for _ in range(quantity))
    return password


# @register.filter(name='get_image_path')