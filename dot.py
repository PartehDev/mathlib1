def dotproduct(vec1, vec2):
    dotproduct=0
    for vec1,vec2 in zip(vec1,vec2):
        dotproduct = dotproduct+vec1*vec2
    return dotproduct