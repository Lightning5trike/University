import Data.Char

type StudentMark = (String, Int)

betterStudent :: StudentMark -> StudentMark -> String
betterStudent (s1, m1) (s2, m2)
  | m1 >= m2 = s1
  | otherwise = s2

marks :: [StudentMark] -> [Int]
marks stmks = [mk | (st, mk) <- stmks]

pass :: [StudentMark] -> [String]
pass stmks = [st | (st, mk) <- stmks, mk >= 40]

-- An example list of student marks
testData :: [StudentMark]
testData =
  [ ("John", 53),
    ("Sam", 16),
    ("Kate", 85),
    ("Jill", 65),
    ("Bill", 37),
    ("Amy", 22),
    ("Jack", 41),
    ("Sue", 71)
  ]

addPairs :: [(Int, Int)] -> [Int]
addPairs pairList = [i + j | (i, j) <- pairList]

minAndMax :: Int -> Int -> (Int, Int)
minAndMax x y
  | x <= y = (x, y)
  | otherwise = (y, x)


-- 1
sumDifference :: Int -> Int -> (Int, Int)
sumDifference x y = (x + y, x - y)


-- 2
grade :: StudentMark -> Char
grade (name, mark)
  | mark < 0 || mark > 100 = error "Mark must be between 0 and 100"
  | mark >= 70 = 'A'
  | mark >= 60 = 'B'
  | mark >= 50 = 'C'
  | mark >= 40 = 'D'
  | mark >= 0 = 'F'


-- 3
capMark :: StudentMark -> StudentMark
capMark (name, mark)
  | mark <= 40 = (name, mark)
  | mark > 40 = (name, 40)
  | otherwise = error "Mark must be between 0 and 100"

-- 4
firstNumbers :: Int -> [Int]
firstNumbers n = [1 .. n]

-- 5
firstSquares :: Int -> [Int]
firstSquares n = [x ^ 2 | x <- firstNumbers n]

-- 6
capitalise :: String -> String
capitalise letters = [toUpper x | x <- letters]

-- 7
onlyDigits :: String -> String
onlyDigits numbers = [x | x <- numbers, isDigit x]

-- 8
capMarks :: [StudentMark] -> [StudentMark]
capMarks x = [capMark mark | mark <- x]

-- 9
gradeStudents :: [StudentMark] -> [(String, Char)]
gradeStudents graded = [(name, grade (name, mark)) | (name, mark) <- graded]

-- 10
duplicate :: String -> Int -> String
duplicate dupe n = concat [dupe | num <- [1 .. n]]

-- 11
divisors :: Int -> [Int]
divisors n = [x | x <- [1 .. n], mod n x == 0]

--12
isPrime :: Int -> Bool
isPrime n = length (divisors n) == 2


--13
split :: [(a, b)] -> ([a], [b])
split lists = ([fst element | element <- lists], [snd element | element <- lists])

split2 :: [(a, b)] -> ([a], [b])
split2 lists = ([x | (x, y) <- lists], [y | (x, y) <- lists])
