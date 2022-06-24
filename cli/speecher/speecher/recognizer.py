from progress.bar import Bar
from vosk import Model, KaldiRecognizer
from color_print import color_print, Colors


class Recognizer:

    def __init__(self, lang: str):
        self.lang = lang

        try:
            self.model = Model(lang=lang)
        except Exception as ex:
            if str(ex) == ('lang %s does not exist', lang):
                color_print('The language selected does not exists!', Colors.FAIL)
                color_print("Please look at https://alphacephei.com/vosk/models for available language models.", Colors.WARNING)
            else:
                raise ex
        pass

    def recognize(self, file: str):

        # Large vocabulary free form recognition
        rec = KaldiRecognizer(self.model, 16000)

        # You can also specify the possible word list
        # rec = KaldiRecognizer(model, 16000, "zero oh one two three four five six seven eight nine")

        wf = open(file, "rb")
        iosize = len(wf.read())
        bar = Bar('Analyzing speeche', max=iosize,
                  suffix='%(percent)d%% (%(index)d/%(max)d bytes remaining) - Time elapsed: %(elapsed)ds', fill='@')

        bar.max = iosize

        wf = open(file, "rb")
        wf.read(44)  # skip header
        bar.next(44)

        bar.next(4000)
        rec.SetWords(True)
        rec.SetPartialWords(True)

        while True:
            data = wf.read(4000)
            bar.next(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                pass
                # print(rec.Result())
            else:
                pass
                # print(rec.PartialResult())

        '''while iosize > 0:
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                if res['text'] != '':
                    print(res)
                result.append(res)
            data = wf.read(4000)
            iosize = iosize - 4000
            bar.next(4000)'''
        print('\n')
        print(rec.FinalResult())