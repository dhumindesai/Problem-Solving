def flood_fill(pixel_row, pixel_column, new_color, image):
    def in_valid_neighbor(row, col, old_color):
        return 0 <= row < len(image) and 0 <= col < len(image[0]) and old_color == image[row][col]

    def get_neighbors(node, old_color):
        result = []
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            row = node[0] + x
            col = node[1] + y
            if in_valid_neighbor(row, col,old_color):
                result.append((row, col))

        return result

    def dfs(node, old_color):
        image[node[0]][node[1]] = new_color
        for neighbor in get_neighbors(node, old_color):
            dfs(neighbor, old_color)

    dfs((pixel_row, pixel_column), image[pixel_row][pixel_column])

    return image

print(flood_fill(0,1,2,
[
[0, 1, 3],
[1, 1, 1],
[1, 5, 4]
]))