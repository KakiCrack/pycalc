def bookMeetingRoom(participants):
    if participants < 1:
        raise ValueError("Invalid number of participants")
    elif participants <= 10:
        return "smallRoom"
    elif participants <= 30:
        return "mediumRoom"
    elif participants <= 50:
        return "largeRoom"
    else:
        return "refuse"