
appleSrc="https://embed.music.apple.com/us/album/500lbs/1706351062?i=1706351081"
spotifySrc="https://open.spotify.com/search/500lbs"
appleSrc2="https://embed.music.apple.com/us/album/urrrge-feat-a%24ap-rocky/1739234520?i=1739235288"
spotifySrc2="https://open.spotify.com/search/urrrge-feat-a%24ap-rocky"

def slice_url(url):
    slicedUrl = ""
    finalUrl = ""
    stack = []
    slashCount = 0
    for i in range(len(url)):
        if url[i] == "/" and url[i+1] == "a" and url[i+2] == "l":
            slicedUrl = url[i+6:]
            break

    for i in range(len(slicedUrl)):
        if slicedUrl[i] == "/":
            slashCount += 1
        if slashCount == 2:
            break
        stack.append(slicedUrl[i])

    for i in range(len(stack)):
        finalUrl += stack[i]

    return finalUrl

def convertToSpotify(url):
    spotifyUrl = "https://open.spotify.com/search"
    temp = slice_url(url)
    spotifyUrl += temp
    print(spotifyUrl)

def main():
    print("Apple music version(the better one): ")
    print(appleSrc)
    print("\nAfter being tortured and destroyed and turned into Spotify's version: ")
    convertToSpotify(appleSrc)


if __name__ == '__main__':
    main()


