**7 kyu**
# Koch curve
Koch curve is a simple geometric fractal.

This fractal is constructed as follows: take a segment divided into three equal parts. Instead of the middle part, two identical segments are inserted, set at an angle of 60 degrees to each other.

This process is repeated at each iteration: each segment is replaced by four. You must write a program that takes the number n and returns an array of rotation angles when drawing a line from the starting point to the ending point. The rotation angle is positive in a counterclockwise direction.

![koch curve](https://i2.wp.com/fractal.institute/old/wp-content/uploads/2015/04/748px-Koch_curve_construction.jpg?resize=679%2C697&ssl=1)

Input: An integer `n` (`0 <= n <= 8`)

Output: An array of angles of rotation. The angle of rotation must be in the interval `[-180; 180]`. For example, for `n == 0` should return an empty array and for `n == 1` the answer should be `[60, -120, 60]`
