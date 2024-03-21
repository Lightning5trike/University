--1 
data Month = Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec
    deriving (Show, Eq)
data Season = Winter | Spring | Summer | Autumn
    deriving (Show, Eq)

-- 2  guard   4 lines
season :: Month -> Season
season mon
    | mon == Dec || mon == Jan || mon == Feb  = Winter
    | mon == Mar || mon == Apr || mon == May = Spring
    | mon == Jun || mon == Jul || mon == Aug = Summer
    | mon == Sep || mon == Oct || mon == Nov = Autumn


-- 3
numberOfDays :: Month -> Int -> Int
numberOfDays Apr _ = 30
numberOfDays Jun _ = 30
numberOfDays Sep _ = 30
numberOfDays Nov _ = 30
numberOfDays Feb year
    | year `mod` 4 == 0 = 29
    | otherwise = 28
numberOfDays _ _ = 31

-- 4
data Point = Point Float Float
    deriving (Show)

-- 5
data PositionedShape = PositionedCircle Float Point | PositionedRectangle Float Float Point
    deriving (Show)

-- 6
move :: PositionedShape -> Float -> Float -> PositionedShape
move shape (Point oldX oldY) x y = shape Point (oldX + x) (oldY + y)

myCirc :: PositionedShape
myCirc = PositionedCircle 5.0 (Point 10.0 20.0)
myRect :: PositionedShape
myRect = PositionedRectangle 10.0 20.0 (Point 10.0 20.0)

-- 7
data Tree = Null | Node Int Tree Tree
    deriving (Show)

numberOfNodes :: Tree -> Int
numberOfNodes Null = 0
numberOfNodes (Node _ tree1 tree2) = 1 + numberOfNodes tree1 + numberOfNodes tree2

-- 8
isMember :: Int -> Tree -> Bool
isMember _ Null = False
isMember value (Node n tree1 tree2) 
    | n == value = True
    | otherwise = isMember value tree1 || isMember value tree2

-- 9 
leaves :: Tree -> [Int]
leaves Null = []
-- leaves (Node n Null Null) = [n]
leaves (Node _ tree1 tree2) = leaves tree1 ++ leaves tree2

-- 10
inOrder :: Tree -> [Int]
inOrder Null = []
inOrder (Node n Null Null) = [n]
inOrder (Node n tree1 tree2) = inOrder tree1 ++ [n] ++ inOrder tree2

testBinaryTree :: Tree
testBinaryTree = Node 5 (Node 1 Null Null) (Node 8 (Node 7 Null Null) Null)

-- 11
insert :: Int -> Tree -> Tree
insert value Null = Node value Null Null
insert value (Node n tree1 tree2) 
    | value < n = Node n (insert value tree1) tree2
    | otherwise = Node n tree1 (insert value tree2)

-- 12
listToSearchTree :: [Int] -> Tree
listToSearchTree = foldr insert Null

binaryTreeSort :: [Int] -> [Int]
binaryTreeSort lst = inOrder (listToSearchTree lst)