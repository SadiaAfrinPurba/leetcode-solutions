class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [{} for _ in range(length)]
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snap_id] =  val
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.arr[index]
        if snap_id in snaps:
            return snaps[snap_id]
        else:
            last_val = 0
            for i in range(0, self.snap_id + 1):
                if i in snaps:
                    last_val = snaps[i]
                if i >= snap_id:
                    return last_val
                
            return last_val
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)