class Queue:
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join(self.queue)
    def push(self, data):
        self.queue.append(data)
    def pop(self):
        return self.queue.pop(0) if self.size() != 0 else 'Empty'
    def size(self):
        return len(self.queue)

def display(normal, exp_normal, mistake, mirror, exp_mirror):
    print('NORMAL :')
    print(len(normal))
    print(''.join(str(a) for a in reversed(normal)) if len(normal) != 0 else 'Empty')
    print(f'{exp_normal} Explosive(s) ! ! ! (NORMAL)')
    if mistake != 0:
        print(f'Failed Interrupted {mistake} Bomb(s)')
    print('------------MIRROR------------')
    print(': RORRIM')
    print(len(mirror))
    print(''.join(str(a) for a in reversed(mirror)) if len(mirror) != 0 else 'ytpmE')
    print(f'(RORRIM) ! ! ! (s)evisolpxE {exp_mirror}')


normal, mirror = input('Enter Input (Normal, Mirror) : ').split()
normal = list(normal)
mirror = list(mirror)
q = Queue()

bomb_mirror = []
exp_mirror = 0
for i in range(-1, -len(mirror) - 1, -1):
    bomb_mirror.append(str(mirror[i]))
    if len(bomb_mirror) > 2:
        if bomb_mirror[-1] == bomb_mirror[-2] == bomb_mirror[-3]:
            q.push(str(mirror[i]))
            exp_mirror += 1
            for a in range(3):
                bomb_mirror.pop()

bomb_normal = []
exp_normal = 0
mistake = 0
for i, data in enumerate(normal):
    bomb_normal.append(data)
    if len(bomb_normal) > 2:
        if bomb_normal[-1] == bomb_normal[-2] == bomb_normal[-3]:
            bq_pop = q.pop()
            if data == bq_pop:
                for a in range(2):
                    bomb_normal.pop()
                mistake += 1
            elif bq_pop == 'Empty':
                for a in range(3):
                    bomb_normal.pop()
                exp_normal += 1
            else:
                bomb_normal.insert(-1, bq_pop)
                
display(bomb_normal, exp_normal, mistake, bomb_mirror, exp_mirror)