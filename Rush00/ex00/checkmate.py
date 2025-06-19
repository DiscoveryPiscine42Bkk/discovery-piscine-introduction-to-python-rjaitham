def is_king_in_check(board):
    # ค้นหาตำแหน่งของกษัตริย์
    king_pos = None
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    # หากไม่พบกษัตริย์ในกระดาน
    if not king_pos:
        print("Error: King not found.")
        return
    
    kx, ky = king_pos
    
    # ทิศทางที่ชิ้นส่วนหมากรุกสามารถโจมตีได้
    directions = [
        (-1, 0), (1, 0),  # แนวตั้ง (ขึ้น, ลง)
        (0, -1), (0, 1),  # แนวนอน (ซ้าย, ขวา)
        (-1, -1), (1, 1), # ทแยงมุม (บนซ้าย, ล่างขวา)
        (-1, 1), (1, -1)  # ทแยงมุม (บนขวา, ล่างซ้าย)
    ]
    
    # ตรวจสอบทิศทางการโจมตีจากชิ้นส่วนต่างๆ
    for dx, dy in directions:
        x, y = kx, ky
        while 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
            x += dx
            y += dy
            piece = board[x][y]
            if piece != '.':  # พบชิ้นส่วน
                if piece == 'P':  # เบี้ยสามารถโจมตีทแยงมุม
                    if abs(dx) == 1 and abs(dy) == 1:
                        print("Success")
                        return
                elif piece == 'R':  # โกหกสามารถโจมตีในแนวตั้งหรือแนวนอน
                    if dx == 0 or dy == 0:
                        print("Success")
                        return
                elif piece == 'B':  # โยนข้ามสามารถโจมตีในทแยงมุม
                    if abs(dx) == 1 and abs(dy) == 1:
                        print("Success")
                        return
                elif piece == 'Q':  # ราชินีสามารถโจมตีในทุกทิศทาง
                    if dx == 0 or dy == 0 or (abs(dx) == 1 and abs(dy) == 1):
                        print("Success")
                        return
                break  # หยุดตรวจสอบในทิศทางนี้

    # หากไม่มีชิ้นส่วนใดที่สามารถโจมตีได้
    print("Fail")