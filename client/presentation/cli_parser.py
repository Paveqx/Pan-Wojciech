import argparse

def get_parser():
    parser = argparse.ArgumentParser(prog="orator")
    parser.add_argument("text", nargs="?", help="Tekst do wypowiedzenia")
    parser.add_argument("-o", "--output", help="Ścieżka zapisu pliku audio")
    parser.add_argument("-s", "--source", help="Plik tekstowy jako źródło")
    parser.add_argument("--rate", type=int, help="Prędkość mowy")
    parser.add_argument("--volume", type=float, help="Głośność mowy")
    parser.add_argument("--voice", help="ID głosu (voice)")
    return parser