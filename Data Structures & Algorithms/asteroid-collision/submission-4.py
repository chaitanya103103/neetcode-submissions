class Solution:
    def asteroidCollision(self, asteroids):

        while True:
            collision = False

            for i in range(len(asteroids) - 1):

                if asteroids[i] > 0 and asteroids[i + 1] < 0:

                    collision = True

                    if abs(asteroids[i]) > abs(asteroids[i + 1]):
                        asteroids.pop(i + 1)

                    elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                        asteroids.pop(i)

                    else:
                        asteroids.pop(i + 1)
                        asteroids.pop(i)

                    break

            if collision == False:
                return asteroids