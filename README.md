# AI_Connect4_MiniMax & Q-learning

The default algorithm is a method which would check if there is any possibility of winning or losing for the current step first of all. If there is an empty position could make the default player win or lose, the default player would occupy this position. If not, the default player would choose a random position from all of the empty positions.

For classic connect 4, there are 4,531,985,219,092 possible boards, it’s impossible for minimax to keep iteration to get to the game end for every board. So I added a depth limitation to the minimax algorithm, if the depth came to 6 and the game did not end, the minmax iteration function would return 0. And I also resized the board to 5x6 to reduce the calculation because my computer is not strong enough. 

To compare the minimax and default algorithm, a total of 1000 games were played, and who plays first is also random. The results are shown below, the Minimax win probability is around 80%, the default win probability is around 10%, and the tied game probability is near 10%. Theoretically, the minimax should never lose if we can calculate every iteration. However, because of the limitation of computing, the max iteration depth is 6 here, and the result is also acceptable.

![1](https://github.com/Weiwei-Wan/AI_Connect4_MiniMax-Q-learning/assets/74362292/07b4d83a-7750-462d-9fc7-e2cd0ad20618)

# Tabular Q-learning playing against default opponent
Theoretically,  the tabular Q learning algorithm could win all the games because connect4 is a solved game. Here the Q learning algorithm played with the default algorithm for 100,000 games, and the Q table also kept updating by playing. The results are shown below. From the results we can conclude that as the number of games increases, the winning rate of Q learning also increases. For connect4, improving training numbers can improve the win probability, but it’s impossible to cover the entire state of the game. To solve this problem, we need deep Q learning to get rid of the Q table and replace it with a Deep Neural Network.

![2](https://github.com/Weiwei-Wan/AI_Connect4_MiniMax-Q-learning/assets/74362292/cb18bf30-d5f5-42d8-9e2f-265a9911f3b1)

# Tabular Q-learning playing against Minimax

In Tic Tac Toe, the Q learning and minimax algorithm could never beat each other, because both of the two algorithms are perfect in Tic Tac Toe. However in Connect4, because of the computing and storage limitation, the minimax algorithm could not get to the game end depth, and the Q learning algorithm could not cover all of the game board states, both algorithms are not perfect. Here the Q learning algorithm played with the minimax algorithm for 500 games, and the Q table also kept updating by playing. The results are shown below. From the results we can conclude that as the number of games increases, the win probability of Q learning also improves. And after 500 games, the overall win probability of Q learning is near 90%, and the overall win probability of minimax is near 10%. Q learning has better performance here, maybe because the minimax algorithm’s strategy is regular and predictable, the Q table can get the same state and win the game.

![3](https://github.com/Weiwei-Wan/AI_Connect4_MiniMax-Q-learning/assets/74362292/e431caeb-8cfa-43cc-9af8-1a48122298aa)

# How to run: 

run PlayerVsPlayer.py
lin 145: play(player1 = 1, player2 = 2, play_number = 1000, q_learning_train_number = 100000), 
0: defalt  1: minimax  2:q learning
change parameter if you want
