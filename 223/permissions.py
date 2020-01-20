def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
       its octal representation.

       In Unix you have user, group and other permissions,
       each can have read (r), write (w), and execute (x)
       permissions expressed by r, w and x.

       Each has a number:
       r = 4
       w = 2
       x = 1

       So this leads to the following input/ outputs examples:
       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """

    def count(ugo: str) -> str:
        value = 0
        for k, v in enumerate(ugo):
            if v == "r":
                value += 4
            if v == "w":
                value += 2
            if v == "x":
                value += 1
        return str(value)
    # :3
    user = rwx[:3]
    group = rwx[3:6]
    # 6:
    other = rwx[6:]
    # :D
    return count(user) + count(group) + count(other)

