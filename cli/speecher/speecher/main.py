# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.from vosk import Model, KaldiRecognizer, SetLogLevel
import argparse
from progress.bar import Bar
from vosk import Model, KaldiRecognizer


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(file: str, lang: str):
    try:
        model = Model(lang=lang)
    except Exception as ex:
        if str(ex) == ('lang %s does not exist', lang):
            print(bcolors.FAIL + 'The language selected does not exists!' + bcolors.ENDC)
            print(bcolors.WARNING + "Please look at https://alphacephei.com/vosk/models for available language models." + bcolors.ENDC)
        else:
            raise ex
    # Large vocabulary free form recognition
    rec = KaldiRecognizer(model, 16000)

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
            #print(rec.Result())
        else:
            pass
            #print(rec.PartialResult())

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("test")
    prs = argparse.ArgumentParser(description='Transform a wav file to a text file.')
    prs.add_argument('--lang', dest='lang', type=str, default='en-us', required=False,
                     help='The language of the audio file')
    prs.add_argument('--file', dest='file', type=str, required=True, help='The audio file')
    args = prs.parse_args()
    main(args.file, args.lang)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
