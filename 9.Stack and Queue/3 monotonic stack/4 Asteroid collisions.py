def asteroid(nums):
    stack = []
    result = []
    for i in nums:
        while len(stack)>=2:
            a = stack.pop()
            b = stack.pop()
            if (int(a)>0 and int(b)<0) or (int(a<0) & int(b>0)) :
                result.append(max(abs(a),abs(b)))
                stack.append(max(abs(a),abs(b)))
            else:
                result.append(max(abs(a),abs(b)))
                stack.append(max(abs(a),abs(b)))
        stack.append(nums)
    return result

print(asteroid([5,10,-5]))