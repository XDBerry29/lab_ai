graph [  directed 0  node [    id 0    label "Proteins"  ]
  node [    id 1    label "Hemoglobin"    organism "Human"    function "Oxygen Transport"    gene "HBB"  ]
  node [    id 2    label "Insulin"    organism "Human"    function "Regulation of Blood Sugar"    gene "INS"  ]
  node [    id 3    label "Green Fluorescent Protein (GFP)"    organism "Jellyfish"    function "Fluorescent Tagging"    gene "GFP"  ]
  node [    id 4    label "Collagen"    organism "Various"    function "Structural Support"    gene "COL1A1"  ]
  node [    id 5    label "Cytochrome c"    organism "Various"    function "Electron Transport"    gene "CYCS"  ]
  node [    id 6    label "Actin"    organism "Various"    function "Cellular Structure and Movement"    gene "ACTA1"  ]
  node [    id 7    label "Myosin"    organism "Various"    function "Muscle Contraction"    gene "MYH7"  ]
  edge [    source 1    target 0  ]
  edge [    source 2    target 0  ]
  edge [    source 3    target 0  ]
  edge [    source 4    target 0  ]
  edge [    source 5    target 0  ]
  edge [    source 6    target 0  ]
  edge [    source 7    target 0  ]
  edge [    source 1    target 5  ]
  edge [    source 5    target 6  ]
  edge [    source 6    target 7  ]
  edge [    source 7    target 1  ]
  edge [    source 6    target 4  ]
  edge [    source 2    target 4  ]
  edge [    source 3    target 4  ]
  edge [    source 1    target 4  ]
]