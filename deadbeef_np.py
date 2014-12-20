import commands
import weechat

def weechat_np(data, buffer, args):
    read_track = commands.getoutput('deadbeef --nowplaying "%a - (%b) - %t [%@:BPS@bit / %@:BITRATE@kbps / %@:SAMPLERATE@Hz]"').split('\n')
    weechat.command(buffer, '/me is currently listening to: ' + read_track[1])
    return weechat.WEECHAT_RC_OK

weechat.register("deadbeef_np", "mwgg", "0.9", "MIT", "Show name of the song currently played by DeaDBeeF", "", "")
weechat.hook_command("np", "Get/send now playing info.", "", "", "", "weechat_np", "")
