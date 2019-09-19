import argparse
import onebusaway


def main(args):
    oba_client = onebusaway.OneBusAwayClient(args.agency_id, args.api_key)
    print(str(oba_client.get_arrivals_and_departures_for_stop(args.stop_id)))


def get_parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', help="OBA API key", required=True)
    parser.add_argument('--agency-id', help="OBA agency ID", default="1")
    parser.add_argument('--stop-id', help="Agency stop ID", default="468")
    return parser.parse_args()


if __name__ == '__main__':
    main(get_parsed_args())
