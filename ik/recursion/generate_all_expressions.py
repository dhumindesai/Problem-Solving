def evaluate(slate):
    return True


def generate_all_expressions(s, target):
    result = []

    def helper(i, slate):

        #backtracking condition
        # if total > target:
        #     return

        # leaf nodes
        if i == len(s):
            expr = "".join(slate)
            # print(expr)
            if evaluate(slate):
                result.append(expr)
            return

        # internal nodes
        else:
            # join
            slate.append(s[i])
            helper(i + 1, slate)
            slate.pop()

            # +
            slate.append("+" + s[i])
            helper(i + 1, slate)
            slate.pop()

            # *
            slate.append("*" + s[i])
            helper(i + 1, slate)
            slate.pop()

    helper(1, [s[0]])

    return result

# def generate_all_expressions(s, target):
#     if not s:
#         return []
#     output = []
#
#     def _dfs(so_far, evaluated, idx, prev):
#         if idx == len(s):
#             if evaluated == target:
#                 output.append(so_far)
#             return
#
#         for i in range(idx, len(s)):
#             curr = s[idx:i+1]
#             curr_int = int(curr)
#             if idx == 0:
#                 _dfs(so_far + curr, curr_int, i+1, curr_int)
#             else:
#                 _dfs(so_far + '+' + curr, evaluated+curr_int, i+1, curr_int)
#                 _dfs(so_far + '*' + curr, (evaluated-prev) + (prev*curr_int), i+1, prev*curr_int)
#
#     _dfs('', 0, 0, 0)
#     return output

print(generate_all_expressions("1234", 11))
print(generate_all_expressions("222", 24))
print(generate_all_expressions("99", 99))