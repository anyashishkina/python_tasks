file_content = open('26-61.txt')
file_lines = file_content.split('\n')
image_number, image_volume = file_lines[0].split()

images = [int(x) for x in file_lines[1:] if x]
images.sort()
s, cnt, max_volume = 0, 0, 0

for image in images:
    if image >= 101:
        if s < (image_volume//2):
            s += image
            cnt += 1


for image in images:
    if image < 101:
        if s < image_volume:
            s += image
            cnt += 1
            max_volume = max(max_volume, image)

print(cnt, max_volume)
