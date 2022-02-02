def floodFill(img,row,col,p):
    start = img[row][col]
    queue = [(row,col)]
    visited = set()
    while len(queue) > 0 :
        row,col = queue.pop(0)
        visited.add((row,col))
        img[row][col] = p
        for row,col in neighbours(img,row,col,start):
            if (row,col) not in visited:
                queue.append((row,col))
    return img

def neighbours(img,row,col,start):
    indices = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
    return [(row,col) for row,col in indices if isValid(img,row,col) and img[row,col]==start]

def isValid(img,row,col):
    return row>=0 and row<len(img) and col>=0 and col<len(img[0])