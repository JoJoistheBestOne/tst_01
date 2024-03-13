

class Tploss(object):
    def run(self, featss, labelss, margin=0.3):
        featss = F.normalize(featss, dim=-1)
        b, d = featss.shape
        pos_ind = labelss == labelss.t() # b 0 0 1 0 1 
        neg_ind = labelss != labelss.t()
        # mask = ...
        simss  = featss@featss.t()
        mask = 1- torch.eye(b)
        simss=simss * mask

        # mining..

        loss = -(simss[pos_ind] - simss[neg_ind] - margin) # d


