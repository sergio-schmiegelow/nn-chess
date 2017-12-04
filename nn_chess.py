'''Project to develop a neural network based chess player'''
import numpy as np
import unittest


whiteSideStartBoard = 'RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr'
blackSideStartBoard = 'RNBKQBNRPPPPPPPP................................pppppppprnbkqbnr'
#-------------------------------------------------------------------------
def stringToNpArray(boardString):
    '''Return the board string on 2D (8x8) numpy array format
    The inverse operation is just numpy.ndarray.tostring()'''
    return np.frombuffer(boardString, dtype = np.int8, count=64).reshape((8,8))
#-------------------------------------------------------------------------
def stringToStringArray(boardString):
    '''Return the board on the string array, starting on the opponent side, to
    be confortable to read after printing on a terminal'''
    stringArray = []
    for i in range(7,-1,-1):
        stringArray.append(boardString[i*8: (i+1)*8])
    return stringArray
#-------------------------------------------------------------------------
def stringArrayToString(boardStringArray):
    '''Reverse of stringToStringArray'''
    string = boardStringArray[7]
    for i in range(6,-1,-1):
        string += boardStringArray[i]
    return string
#-------------------------------------------------------------------------
def generatePawnMoveBoards(location, currentBoard):
    '''Returns a list of all possible boards produced by the movement of a
    pawn on location'''
    currentBoardArray = stringToNpArray(currentBoard)
    #IMPLEMENTAR
    return []
#-------------------------------------------------------------------------
def generatePieceMoveBoards(pieceLocation, currentBoard):
    '''Returns a list of all possible boards produced by the movement of a
    piece on location'''
    currentBoardArray = stringToNpArray(currentBoard)
    piece = chr(currentBoardArray[pieceLocation[0], pieceLocation[1]])
    if piece == 'P':
        nextBoards = generatePawnMoveBoards(pieceLocation, currentBoard)
    else:
        print "movement of piece %c is not supported"%piece
    return nextBoards
#-------------------------------------------------------------------------
def tddCompareMoveBoards(currentBoard, pieceLocation, expectedBoards):
    '''Returns True if the possibleBoards are different
    of the expected boards'''
    possibleBoards = generatePieceMoveBoards(pieceLocation, currentBoard)
    if len(possibleBoards) != len(expectedBoards):
        return True
    print "equal sizes"
    for nextBoard in nextBoard:
        if nextBoard not in possibleBoards:
            return True
    print "equal contents"
    return False
#-------------------------------------------------------------------------
class testMoveBoards(unittest.TestCase):
    def testBoardConversions(self):
        self.assertTrue(np.array_equal(stringToNpArray(whiteSideStartBoard),
                    np.array([[ 82,  78,  66,  81,  75,  66,  78,  82],
                              [ 80,  80,  80,  80,  80,  80,  80,  80],
                              [ 46,  46,  46,  46,  46,  46,  46,  46],
                              [ 46,  46,  46,  46,  46,  46,  46,  46],
                              [ 46,  46,  46,  46,  46,  46,  46,  46],
                              [ 46,  46,  46,  46,  46,  46,  46,  46],
                              [112, 112, 112, 112, 112, 112, 112, 112],
                              [114, 110,  98, 113, 107,  98, 110, 114]])))
        self.assertEqual(stringToNpArray(whiteSideStartBoard).tostring(), whiteSideStartBoard)
        self.assertEqual(stringToStringArray(whiteSideStartBoard),
                         ['rnbqkbnr',
                          'pppppppp',
                          '........',
                          '........',
                          '........',
                          '........',
                          'PPPPPPPP',
                          'RNBQKBNR'])
        self.assertEqual(stringArrayToString(stringToStringArray(whiteSideStartBoard)), whiteSideStartBoard)
#-------------------------------------------------------------------------
    def testPawnMoves(self):
        #pawn first move
        print "testing pawn moves"
        self.assertFalse(tddCompareMoveBoards(stringArrayToString(['rnbqkbnr',
                                                                   'pppppppp',
                                                                   '........',
                                                                   '........',
                                                                   '........',
                                                                   '........',
                                                                   'PPPPPPPP',
                                                                   'RNBQKBNR']),
                                                                   [1, 1],
                                             [stringArrayToString(['rnbqkbnr',
                                                                   'pppppppp',
                                                                   '........',
                                                                   '........',
                                                                   '........',
                                                                   '..P.....',
                                                                   'PP.PPPPP',
                                                                   'RNBQKBNR']),
                                              stringArrayToString(['rnbqkbnr',
                                                                   'pppppppp',
                                                                   '........',
                                                                   '........',
                                                                   '..P.....',
                                                                   '........',
                                                                   'PP.PPPPP',
                                                                   'RNBQKBNR'])]))
#-------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
