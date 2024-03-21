import Prelude hiding (reverse)

{- Week6.hs
 This module illustrates the use of functions as values
-}

import Data.Char

twice :: (Int -> Int) -> Int -> Int
twice f x = f (f x)

multiply :: Int -> Int -> Int
multiply x y = x * y

double :: Int -> Int
double = multiply 2

doubleAll :: [Int] -> [Int]
doubleAll = map (*2)

areDigits :: String -> [Bool]
areDigits = map isDigit

keepPositive :: [Int] -> [Int]
keepPositive = filter (>0)

keepDigits :: String -> String
keepDigits = filter isDigit

addUp :: [Int] -> Int
addUp = foldr (+) 0 

myConcat :: [[a]] -> [a]
myConcat = foldr (++) []


-- 1
mult10 :: [Int] -> [Int]
mult10 = map (*10)

-- 2
onlyLowerCase :: String -> String
onlyLowerCase = filter isLower

-- 3
orAll :: [Bool] -> Bool
orAll = foldr (||) False

-- 4
sumSquares :: [Int] -> Int
sumSquares = foldr (+) 0 . map (^2)

-- 5
filterBetweenZeroAndTen :: Int -> Bool
filterBetweenZeroAndTen x = x >= 0 && x <= 10

zeroToTen :: [Int] -> [Int]
zeroToTen = filter (>=0) . filter (<=10)

-- 6
squareRoots :: [Float] -> [Float]
squareRoots = map sqrt . filter (>=0) 

-- 7
countBetween :: Float -> Float -> [Float] -> Int
countBetween lowerBound upperBound = foldr (\x total -> if x <= upperBound && x >= lowerBound then total + 1 else total) 0 

-- 8
alwaysPositive :: (Float -> Float) -> [Float] -> Bool
alwaysPositive func = foldr (\x acc -> func x >= 0 && acc) True
-------------    all  .   map (>0) .  map func 


-- 9
productSquareRoots :: [Float] -> Float
-- productSquareRoots lst = foldr (*) 1 $ map (\x -> if x >= 0 then sqrt x else 1) lst
-- 13
productSquareRoots lst = foldr (*) 1 $ map sqrt (filter (\x -> x >= 0) lst)

-- 10
removeFirst :: (a -> Bool) -> [a] -> [a]
removeFirst property (x : xs)
    | property x == True = xs
    | otherwise = x : removeFirst property xs

-- 11
removeLast :: (a -> Bool) -> ([a] -> [a])
removeLast property = reverse . removeFirst property . reverse

-- 12
-- zeroToTen :: [Int] -> [Int]
-- zeroToTen lst = filter (\x -> x <= 10 && x >= 0) lst

-- 13
reverse :: [a] -> [a]
reverse lst = foldr (\char string -> string ++ [char]) [] lst