from PIL import Image

def concatenate_images_vertically(num_images):
    # 이미지들을 열기
    images_opened = []

    for i in range(1, num_images + 1):
        image_path = f"{i}.png"
        img = Image.open(image_path)
        images_opened.append(img)

    # 이미지들의 높이 계산
    total_height = sum(img.height for img in images_opened)

    # 세로축 중앙을 기준으로 이미지를 이어붙이기
    result_image = Image.new("RGB", (max(img.width for img in images_opened), total_height), (255, 255, 255))

    current_height = 0
    for img in images_opened:
        result_image.paste(img, ((result_image.width - img.width) // 2, current_height))
        current_height += img.height

    # 결과 이미지 저장 또는 표시
    result_image.show()
    result_image.save("result.jpg")  # 결과 이미지를 파일로 저장하려면 주석을 해제하세요.

# 이어붙일 이미지 파일 경로들을 리스트로 지정
num_images = int(input("이미지는 몇 번까지 있나요?: "))

# 이미지들을 세로로 이어붙이기
concatenate_images_vertically(num_images)