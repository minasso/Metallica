import lyricwikia
artist = 'Metallica'
song = 'the memory remains'
lyrics = lyricwikia.get_lyrics(artist,song)
print(lyrics)

# with open('songs.txt','r') as rf:
#     songs = rf.readlines()
# songs=[s.replace('\n','') for s in songs]
# with open('lyrics.txt','w') as wf:
#     i=0
#     for song in songs:
#         i+=1
#         print(i)
#         song=song
#         try:
#             lyrics = lyricwikia.get_lyrics(artist,song)
#             wf.write(lyrics)
#             wf.write('\n--------------------------------------------------\n')
#         except:
#             wf.write(song + ' lyrics not found')