#!/usr/bin/python3
""" solving lockboxes problem """


def canUnlockAll(boxes):
    """ lockboxes problem """
    unlock = [0]

    for id, keys in enumerate(boxes):
        if not keys:
            continue

        for key in keys:
            if key < len(boxes) and key != id and key not in unlock:
                unlock.append(key)
    return len(boxes) == len(unlock)
