import GHC.Base (VecElem(Int16ElemRep))
helloWorld :: IO ()
helloWorld = putStrLn "Hello, World!"

displayFile :: IO ()
displayFile = do
    putStr "Enter the filename: "
    name <- getLine
    contents <- readFile name
    putStr contents

getInt :: IO Int
getInt = do
    str <- getLine
    return (read str :: Int)

isPalindrome :: String -> String
isPalindrome str
   | str == reverse str  = str ++ " is a palindrome"
   | otherwise           = str ++ " is not a palindrome"

pal :: IO ()
pal = do
    line <- getLine
    let response = isPalindrome line
    putStrLn response

palLines :: IO ()
palLines = do
    putStr "Enter a line: "
    str <- getLine
    if str == "" then
        return ()
    else do
        putStrLn (isPalindrome str)
        palLines

-- 1
name :: IO ()
name = do
    putStrLn "Hello, what's your name?"
    name <- getLine
    putStrLn ("Hey " ++ name ++ ", you rock!")

--2 
addnums :: IO ()
addnums = do
    putStrLn "num1"
    a <- getLine
    putStrLn "num2"
    b <-getLine
    let num1 = read a::Int
    let num2 = read b::Int
    print (num1 + num2)

--3 
copyFileContents :: FilePath -> FilePath -> IO ()
copyFileContents sourceFile destFile = do
    putStrLn "file  name to be copied"
    source <- getLine
    putStrLn "copy file name"
    destination <-getLine
    copyFileContents source destination
    -- Read the contents of the source file
    content <- readFile sourceFile
    writeFile destFile content




--4 
buildStringList :: [String] -> IO ()
buildStringList stringsSoFar = do
    buildStringList []
    putStr "Enter a line: "
    str <-  getLine
    let updatedList = stringsSoFar ++ [str]
    print ("List is now " ++ show updatedList)

--5
sumOfNIntegers :: IO Int
sumOfNIntegers = do
    putStr "Number of ints: "
    n <- readLn :: IO Int
    let totalSum 0 tot = return tot
        totalSum n tot = do
            putStr "Enter an integer: "
            num <- readLn :: IO Int
            totalSum (n - 1) (tot + num)
    -- Start accumulating the sum from n integers
    totalSum n 0







--6
addWord :: [String] -> String -> [String]
addWord wordList word = wordList ++ [word]

wordsToString :: [String] -> String
wordsToString = unlines

wordsOfLength :: Int -> [String] -> [String]
wordsOfLength len = filter (\word -> length word == len)

readFileToList :: FilePath -> IO [String]
readFileToList filePath = do
    -- Read the contents of the file as a single string
    fileContent <- readFile filePath
    -- Convert the string into a list of strings using the 'read' function
    let wordList = read fileContent :: [String]
    return wordList

-- Function to display all words
displayAllWords :: [String] -> IO ()
displayAllWords = writeListToFile "words.txt"

-- Function to write a list of strings back to a file
writeListToFile :: FilePath -> [String] -> IO ()
writeListToFile filePath wordList = writeFile filePath (wordsToString wordList)

programLoop :: [String] -> IO ()
programLoop wordList = do
    putStrLn "\nMenu:"
    putStrLn "1. Add a word to the list"
    putStrLn "2. Display all words"
    putStrLn "3. Display all words of a given length"
    putStrLn "4. Exit"
    putStrLn "Enter your choice: "
    choice <- getLine
    case choice of
        "1" -> do
            putStrLn "Enter the word to add:"
            wordToAdd <- getLine
            let updatedList = addWord wordList wordToAdd
            putStrLn "Word added to the list."
            programLoop updatedList
        "2" -> do
            putStrLn "All words:"
            displayAllWords wordList
            programLoop wordList
        "3" -> do
            putStrLn "Enter the length of words to display:"
            lenStr <- getLine
            let len = read lenStr :: Int
            putStrLn "Words of length " ++ show len ++ ":"
            displayWordsOfLength len wordList
            programLoop wordList
        "4" -> do
            putStrLn "Exiting the program..."
            -- Write the updated list back to 'words.txt' before exiting
            writeListToFile "words.txt" wordList
            putStrLn "Word list has been updated in 'words.txt'."