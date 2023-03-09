if __name__ == "__main__":
    """Print all names defined by defined
    by the compiled module hidden_4.pyc"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        #if does not start with underscores
        if name[:2] != "__":
            print(name)
