import json

def load_file(filename):
    '''Load json file you need'''
    with open(filename, mode='r') as f:
        return json.load(f)

def write_file(filename, obj):
    '''Dump json file you need'''
    with open(filename, mode='w') as f:
        json.dump(obj, f)

def can_do_music_command(ctx):
    '''Check can user do music command'''
    if ctx.author.voice != None and ctx.voice_client != None and ctx.author.voice.channel.id == ctx.voice_client.channel.id:
        return True
    else:
        return False