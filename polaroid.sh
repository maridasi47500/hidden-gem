# Blank space, followed by all JPGs "2-*.png", transparent background, 250x250 pixels each, polaroid effect
#montage null: 2-*.png -background "#0000" -auto-orient -geometry 250x250-10-20 +polaroid ../montage.png

# Thumbnails cropped to square
#mogrify -path thumbs/ -thumbnail 200x200^ -gravity center -extent 200x200 6-*.png

# Montage with squares, without space, on white

# Randomize file order
#mkdir rename

#for i in *.png; do mv $i rename/$(openssl rand -rand $i -hex 8).png; done

montage * +polaroid 15 ./collage.png
