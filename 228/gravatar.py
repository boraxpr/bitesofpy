import hashlib

GRAVATAR_URL = ("https://www.gravatar.com/avatar/"
                "{hashed_email}?s={size}&r=g&d=robohash")


def create_gravatar_url(email, size=200):
    """Use GRAVATAR_URL above to create a gravatar URL.

       You need to create a hash of the email passed in.

       PHP example: https://en.gravatar.com/site/implement/hash/

       For Python check hashlib check out (md5 / hexdigest):
       https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
    """
    email = email.strip().lower()
    m = hashlib.md5()
    m.update(str.encode(email))
    hashed_email = m.hexdigest()
    return GRAVATAR_URL.format(hashed_email=hashed_email, size=size)
