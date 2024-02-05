circumferenceOfCircle :: Float -> Float
circumferenceOfCircle d = pi * d

-- multiply by 10
timesTen :: Int -> Int
timesTen a = a * 10

-- Sum 3 ints
sumThree :: Int -> Int -> Int -> Int
sumThree a b c = a + b + c

-- area of a circle
areaOfCircle :: Float -> Float
areaOfCircle r = pi * r^2

-- volume of cylinder
volumeOfCylinder :: Float -> Float -> Float
volumeOfCylinder  r h = areaOfCircle r * h

-- distance between points
distance :: Float -> Float -> Float -> Float -> Float
distance x1 x2 y1 y2 = sqrt ((y1 - y2) ^ 2 +(x1 - x2)^2)

-- true or false depending on whether equal
threeDifferent :: Int -> Int -> Int -> Bool
threeDifferent a b c = a /= b && b /= c

-- checking if divisible
divisibleBy :: Int -> Int -> Bool
-- divisibleBy a b = a `mod` b == 0
divisibleBy a b = mod a b == 0


-- determine if even
isEven :: Int -> Bool
isEven a = divisibleBy a 2

-- average of 3 ints
averageThree :: Int -> Int -> Int -> Float
averageThree e f g = fromIntegral (e + f + g) / 3

-- 
absolute :: Int -> Int
absolute a = if a < 0 then -a else a