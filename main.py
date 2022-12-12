from literki import Literki
from analyzer import Analyzer
from interface.webapp import WebApp


w = Literki()
# w.new_word()
# print(w)
# print(w.guess('testy'))
# analyzer = Analyzer()
# a = analyzer
# analyzer.load_dictionary('pl.dic')
WebApp(w).start()
