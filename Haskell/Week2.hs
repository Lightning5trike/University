-- q10 with quards
absolute :: Int -> Int
absolute a
    | a < 0 = -a
    | otherwise = a


-- check whether positive or negative using guards
sign :: Int -> Int
sign b
    | b > 0 = 1
    | b == 0 = 0
    | b < 0 = -1

-- check whether equal
howManyEqual :: Int -> Int -> Int -> Int
howManyEqual a b c 
    | a == b && b == c = 3
    | a == c && c /= b || b == c && a /= b || a == b && b /= c = 2
    | a /= b && b /= c = 0

-- length of the diagonal
sumDiagonalLengths :: Float -> Float -> Float -> Float
sumDiagonalLengths d e f = length d + length e + length f
    where
        length z = sqrt (2 * (z^2))

-- taxi difference
taxiFare :: Int -> Float
taxiFare d 
    | d <= 10 = (0.5 * fromIntegral(d)) + 2.2
    | d > 10 = (0.3 * fromIntegral(d)) + 7.2