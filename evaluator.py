from pokereval.hand_evaluator import HandEvaluator


class PokerEvaluator(HandEvaluator):
    @staticmethod
    def evaluate_preflop(hand):

        cards = [c.numerical for c in hand]
        rank = HandEvaluator.Two.evaluate_percentile(cards)
        return rank

    @staticmethod
    def evaluate_flop(hand, board):
        if len(hand) != 2:
            raise ValueError('only two cards!')
        if len(board) != 3:
            raise ValueError('only three cards at flop')
        cards = [c.numerical for c in hand] + [c.numerical for c in board]
        rank = HandEvaluator.Five.evaluate_rank(cards)
        return rank

    @staticmethod
    def evaluate_turn(hand, board):
        if len(hand) != 2:
            raise ValueError('only two cards!')
        if len(board) != 4:
            raise ValueError('only four cards at flop')
        cards = [c.numerical for c in hand] + [c.numerical for c in board]
        rank = HandEvaluator.Six.evaluate_rank(cards)
        return rank

    @staticmethod
    def evaluate_river(hand, board):
        if len(hand) != 2:
            raise ValueError('only two cards!')
        if len(board) != 5:
            raise ValueError('only four cards at flop')
        cards = [c.numerical for c in hand] + [c.numerical for c in board]
        rank = HandEvaluator.Six.evaluate_rank(cards)
        return rank
