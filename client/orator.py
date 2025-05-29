import asyncio
from presentation.cli_parser import get_parser
from api.api_client import ApiClient
from services.client_service import ClientService

BASE_URL = "http://localhost:8000"

async def main():
    parser = get_parser()
    args = parser.parse_args()
    api = ApiClient(BASE_URL)
    svc = ClientService(api)

    # ustawianie parametrów
    if args.rate:
        await svc.set_param('rate', args.rate)
    if args.volume:
        await svc.set_param('volume', args.volume)
    if args.voice:
        await svc.set_param('voice', args.voice)

    # od pliku źródłowego
    if args.source and args.output:
        await svc.from_file(args.source, args.output)
    elif args.source:
        print("Brakuje parametru -o/--output do zapisu")
    # albo pojedynczy tekst
    elif args.text and args.output:
        await svc.download(args.text, args.output)
    elif args.text:
        await svc.speak(args.text)
    else:
        parser.print_help()

if __name__ == "__main__":
    asyncio.run(main())