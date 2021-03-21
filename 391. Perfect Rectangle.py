class Solution:
    def isRectangle(self, rectangles:List[List[int]]) -> bool:
        # ExpectedArea = Sum of all areas of rectangles
        # The areas of rectangles could not overlap.
        
        # initial status of corner positions [(Xm, Ym), (Xm, YM), (XM, Ym), (XM, YM)] and AreaSum
        Xm,Ym, XM, YM = rectangles[0]
        AreaSum = 0
        VisitPosition = set()

        for x1, y1, x2, y2 in rectangles:
            AreaSum += (x2 - x1) * (y2 - y1)
            Xm, Ym, XM, YM = min(Xm, x1), min(Ym, y1), max(XM, x2), max(YM, y2)
            Positions = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for point in Positions:
                if point in VisitPosition:
                    VisitPosition.remove(point)
                else:
                    VisitPosition.add(point)
        # The corners of the small rectangles inside the final large rectangle would be visited twice.
        # We add and remove them and the remaining set would be four corners of the final rectangle.
        # Therefore, we could check the them.
        if ( (XM - Xm)*(YM - Ym) != AreaSum: return False
        if len(VisitPosition) != 4: return False
        return all(corner in VisitPosition for corner in [(Xm, Ym), (Xm, YM), (XM, Ym), (XM, YM)])