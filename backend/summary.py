from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from stop_words import get_stop_words
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.kl import KLSummarizer
import json

def summarization(text):
    
    parser = PlaintextParser.from_string(text, Tokenizer("russian"))

    def getSummary(sumyAlgorithm):
        sumyAlgorithm.stop_words = get_stop_words("russian")
        summary = sumyAlgorithm(parser.document, 2)
        sents = " ".join([str(sentence) for sentence in summary])
        return sents

    stemmer = Stemmer("russian")

    summaries = {}
    # summaries['Luhn'] = getSummary(LuhnSummarizer(stemmer))
    # summaries['SumBasic'] = getSummary(SumBasicSummarizer(stemmer))
    # summaries['LSA'] = getSummary(LsaSummarizer(stemmer))
    summaries['TextRank'] = getSummary(TextRankSummarizer(stemmer))
    # summaries['LexRank'] = getSummary(LexRankSummarizer(stemmer))
    # summaries['KL'] = getSummary(KLSummarizer(stemmer))

    return summaries