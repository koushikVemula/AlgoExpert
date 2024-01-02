def collidingAsteroids(asteroids):
    # Write your code here.
    stack = []
    for i in asteroids :
        if i > 0 :
            stack.append(i)
            continue
        while True :
            if len(stack) == 0 or stack[-1] < 0 :
                stack.append(i)
                break

            size = abs(i)
            if stack[-1] > size :
                break

            if stack[-1] == size :
                stack.pop()
                break

            stack.pop()
    return stack
