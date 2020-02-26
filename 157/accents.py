texts = "Denominada en Euskera como Donostia, está "


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    # 32-127 Basic Latin (The range of a-zA-Z
    # 128-591 = [Latin-1 Supplement, Latin Extended-A, Latin Extended-B]
    return [char for char in text.lower() if ord(char) in range(128, 592)]
