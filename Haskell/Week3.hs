-- We don't import '||' from the prelude, so that we can
-- define our own version

import Prelude hiding (gcd, (&&), (||))

-- The following line declares the || operator (which we are about to
-- re-define) to be right associative and to have precedence 2. This
-- is necessary in order for expressions such as False || x > 2 to be
-- valid (e.g. it sets the precedence of || to be lower than >).

infixr 2 ||

infixr 3 &&

(&&) :: Bool -> Bool -> Bool
True && True = True
False && True = False
True && False = False
False && False = False

-- A naive re-implementation of the Prelude operator ||
(||) :: Bool -> Bool -> Bool
True || True = True
False || True = True
True || False = True
False || False = False


-- 1
(&&) :: Bool -> Bool -> Bool
True && True = True
_ && _ = False

-- (&&) :: Bool -> Bool -> Bool
-- False && _ = False
-- True && a = a

-- An alternative re-implementation
-- (||) :: Bool -> Bool -> Bool
-- False || False   = False
-- _ || _           = True

-- Another alternative re-implementation
-- (||) :: Bool -> Bool -> Bool
-- True || _     =  True
-- False || a    = a

-- fact :: Int -> Int
-- fact n
--   | n == 0 = 1
--   | n > 0 = n * fact (n - 1)
--   | otherwise = error "factorials not defined for negative ints"

-- mult :: Int -> Int -> Int
-- mult n m
--   | n == 0 = 0
--   | n > 0 = m + mult (n - 1) m
--   | otherwise = -mult (-n) m

-- divide :: Int -> Int -> Int
-- divide n m
--   | n < m = 0
--   | otherwise = 1 + divide (n - m) m

-- 2
exOr :: Bool -> Bool -> Bool
exOr True False = True
exOr False True = True
exOr _ _ = False

-- 3
ifThenElse :: Bool -> Int -> Int -> Int
ifThenElse True x _ = x
ifThenElse False _ y = y

-- 4
daysInMonth :: Int -> Int
daysInMonth 2 = 28
daysInMonth x
  | even x = 30
  | otherwise = 31

-- daysInMonth 4 = 30
-- daysInMonth 6 = 30
-- daysInMonth 9 = 30
-- daysInMonth 11 = 30
-- daysInMonth _ = 31

-- preevious question
validDate :: Int -> Int -> Bool
validDate day month = month >= 1 && month <= 12 && day >= 1 && day <= daysInMonth month


-- 5
sumNumbers :: Int -> Int
sumNumbers 0 = 0
sumNumbers x = x + sumNumbers (x - 1)

-- 6
sumSquares :: Int -> Int
sumSquares 0 = 0
sumSquares x = x ^ 2 + sumSquares (x - 1)

-- 7
power :: Int -> Int -> Int
power _ 0 = 1
power x y = x * power x (y - 1)

-- 8
sumFromTo :: Int -> Int -> Int
sumFromTo x y
  | y > x = 0
  | otherwise = sumFromTo x (y - 1) + y


-- 9
gcd :: Int -> Int -> Int
gcd x y
  | x == y = x
  | x > y = gcd (x - y) y
  | otherwise = gcd x (y - x)


-- 10
intSquareRoot :: Int -> Int
intSquareRoot n = findRoot n n

findRoot :: Int -> Int -> Int
findRoot n s
  | s * s <= n && (s + 1) * (s + 1) > n = s
  | s * s > n = findRoot n (s - 1)
  | otherwise = findRoot n (s + 1)
