Vim�UnDo� �9m7T�T=�[m>�/���G���S���e���;>   w             w         %       %   %   %    el�O    _�                            ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         9      6        padding_idx     = kwargs.get('padding_idx', 0)5��                        Z              	       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         :              5��                         Z                     �                        Z                    �                        Z                    �                        Z                    �                        Z                    �                         g                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         :              window_size =5��                         f                     �                         j                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         :              window_size     =5��                         k                     5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         :      &        window_size     = kwargs.get()5��       %                  w                     5�_�                       &    ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         :      (        window_size     = kwargs.get('')5��       &                  x                     �       &                 x                    �       1                  �                     5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         :      3        window_size     = kwargs.get('window_size')5��       2                  �                     �       2                 �                    5�_�      	                 6    ����                                                                                                                                                                                                                                                                                                                                                             el8�     �         :      7        window_size     = kwargs.get('window_size', '')5��       4                 �                    5�_�      
           	      K    ����                                                                                                                                                                                                                                                                                                                                         K       v   K    el9     �         :      L        self.e2h = nn.Linear((window_size - 1) * embedding_size, hidden_dim)5��       J                  N                     �       I                  M                     �       H                 L                    5�_�   	              
      '    ����                                                                                                                                                                                                                                                                                                                                         K       v   K    el9'     �         :      4        self.h2o = nn.Linear(hidden_dim, vocab_size)5��       &                  x                     �       %                  w                     �       $                 v                    5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                         K       v   K    el9-     �         :       5��                          #                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                         K       v   K    el9.     �         ;       5��                          #                      �                        /                     �                        3                     �                        0                     �                        0                     �                        >                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                         K       v   K    el98     �         ;       import torch.functional as FNNLM5��                         B                      �                         A                      �                         ?                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                         K       v   K    el9Y    �         ;      import torch.functional as F5��                         0                      �                        2                     5�_�                       A    ����                                                                                                                                                                                                                                                                                                                                                             el9o    �         ;      B        self.embeddings = nn.Embedding(vocab_size, embedding_size)5��       A                  "                     �       C                 $                    �       C                 $                    �       N                 /                    �       O                 0                    �       O                 0                    �       O                 0                    5�_�                   '       ����                                                                                                                                                                                                                                                                                                                            0          0          v       el:�     �   /   1   ;      %        embeddings = self.EMB(inputs)�   &   (   ;      T        self.EMB = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    &                     	                     �    /                     9                     5�_�                    '       ����                                                                                                                                                                                                                                                                                                                            0          0          v       el:�     �   /   1   ;      $        embeddings = self.EM(inputs)�   &   (   ;      S        self.EM = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    &                                          �    /                     7                     5�_�                    '       ����                                                                                                                                                                                                                                                                                                                            0          0          v       el:�     �   /   1   ;      #        embeddings = self.E(inputs)�   &   (   ;      R        self.E = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    &                                          �    /                     5                     5�_�                    0       ����                                                                                                                                                                                                                                                                                                                            0          0          v       el:�     �   '   )   =       �   (   )   =    �   '   )   <    �   &   (   <      [        self.embeddings = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)�   0   2   <       �   1   2   <    �   0   2   ;    �   /   1   ;      "        embeddings = self.(inputs)�   &   (          Q        self. = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)�   0   1   ;    �   0   1   ;    �   0   1   ;    �   0   1   ;    �   0   1   ;    5��    /                     5                     �    &           Q       R   �      Q       R       �    /           #       $         #       $       �    &           R       S   �      R       S       �    /           $       %         $       %       �    &           S       T   �      S       T       �    /           %       &         %       &       �    &           T       U   �      T       U       �    /           &       &         &       &       �    /                 
   9             
       �    &           U       [   �      U       [       �    /           ,       ,   %      ,       ,       �    &           [       [   �      [       [       �    /           ,       ,   %      ,       ,       �    /   $                  I                     �    0                      J              	       �    0                     J                    �    &          D                 D               �    '                                    	       �    '                  K                K       5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =              (inputs)�   '   )   =      K        = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                          �    1                     X                     5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =             (inputs)�   '   )   =      J       = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                          �    1                     V                     5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =            (inputs)�   '   )   =      I      = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                          �    1                     T                     5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =           (inputs)�   '   )   =      H     = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                          �    1                     R                     5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =          (inputs)�   '   )   =      G    = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                          �    1                     P                     5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =         (inputs)�   '   )   =      F   = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                          �    1                     N                     5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =      
  (inputs)�   '   )   =      E  = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                          �    1                     L                     5�_�                    (        ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   1   3   =      	 (inputs)�   '   )   =      D = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    '                                           �    1                      J                     5�_�                    '        ����                                                                                                                                                                                                                                                                                                                            1          1          v       el:�     �   /   1   <      $        embeddings = self.embeddings   (inputs)�   &   (   =              self.embeddings   C= nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    &                                          �    /   $                  H                     5�_�                     )       ����                                                                                                                                                                                                                                                                                                                            6   !       6   #       v   !    el:�     �   5   7   ;      7        packed_outputs, _ = self.RNN(packed_embeddings)�   4   6   ;              # RNN forward-pass�   (   *   ;      T        self.RNN = nn.GRU(embedding_size, hidden_size, num_layers, batch_first=True)5��    (                     e                     �    4                                          �    5   #                  4                     5�_�      !               )       ����                                                                                                                                                                                                                                                                                                                            6   !       6   #       v   !    el:�     �   5   7   ;      6        packed_outputs, _ = self.RN(packed_embeddings)�   4   6   ;              # RN forward-pass�   (   *   ;      S        self.RN = nn.GRU(embedding_size, hidden_size, num_layers, batch_first=True)5��    (                     d                     �    4                                          �    5   "                  1                     5�_�       "           !   )       ����                                                                                                                                                                                                                                                                                                                            6   !       6   #       v   !    el:�     �   5   7   ;      5        packed_outputs, _ = self.R(packed_embeddings)�   4   6   ;              # R forward-pass�   (   *   ;      R        self.R = nn.GRU(embedding_size, hidden_size, num_layers, batch_first=True)5��    (                     c                     �    4   
                  �                     �    5   !                  .                     5�_�   !   #           "   6   !    ����                                                                                                                                                                                                                                                                                                                            6   !       6   #       v   !    el:�    �   5   7   ;      4        packed_outputs, _ = self.(packed_embeddings)�   4   6                  #  forward-pass�   (   *          Q        self. = nn.GRU(embedding_size, hidden_size, num_layers, batch_first=True)�   6   7   ;    �   6   7   ;    �   6   7   ;    5��    5   !                  .                     �    (           Q       R   V      Q       R       �    4                     �                    �    5           5       6         5       6       �    (           R       S   V      R       S       �    4                     �                    �    5           6       7         6       7       �    (           S       T   V      S       T       �    4                     �                    �    5           7       7         7       7       �    (           T       T   V      T       T       �    4                     �                    �    5           7       7         7       7       5�_�   "   $           #   "   :    ����                                                                                                                                                                                                                                                                                                                                                             el;�     �   !   #   ;      ;        embedding_size  = kwargs.get('embedding_size', 300)5��    !   7                 N                    5�_�   #   %           $   #   7    ����                                                                                                                                                                                                                                                                                                                                                             el;�    �   "   $   ;      8        hidden_size     = kwargs.get('hidden_size', 128)5��    "   4                 �                    5�_�   $               %   ;       ����                                                                                                                                                                                                                                                                                                                                                             el�N    �   v                     �   w            �   w            �   w            �   w            �   u               �   v            �   t                    �   u            �   u            �   u            �   u            �   u            �   u            �   s                  �   t            �   t            �   t            �   t            �   t            �   t            �   t            �   t            �   t            �   t            �   r                �   s            �   s            �   s            �   s            �   s            �   s            �   s            �   q                   �   r            �   r            �   r            �   r            �   r            �   r            �   r            �   r            �   r            �   r            �   r            �   p                  �   q            �   q            �   q            �   q            �   q            �   q            �   q            �   q            �   o                �   p            �   p            �   p            �   m               �   n            �   n            �   n            �   n            �   n            �   n            �   n            �   n            �   n            �   l                �   m            �   m            �   m            �   m            �   j                   �   k            �   k            �   k            �   k            �   k            �   i                �   j            �   j            �   j            �   j            �   j            �   j            �   j            �   j            �   j            �   j            �   j            �   j            �   j            �   h                �   i            �   i            �   i            �   i            �   i            �   i            �   i            �   g                 �   h            �   h            �   h            �   h            �   h            �   h            �   h            �   h            �   h            �   h            �   h            �   h            �   f               �   g            �   g            �   g            �   g            �   g            �   g            �   g            �   g            �   e               �   f            �   f            �   f            �   d               �   e            �   e            �   e            �   e            �   e            �   b                �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   c            �   a               �   b            �   b            �   b            �   b            �   b            �   b            �   b            �   b            �   `                  �   a            �   a            �   a            �   a            �   a            �   a            �   a            �   _                  �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   `            �   ^               �   _            �   _            �   _            �   _            �   _            �   _            �   _            �   _            �   _            �   \                �   ]            �   ]            �   ]            �   ]            �   ]            �   ]            �   ]            �   [                   �   \            �   \            �   \            �   \            �   \            �   \            �   \            �   \            �   \            �   \            �   \            �   \            �   \            �   Z               �   [            �   [            �   [            �   [            �   Y               �   Z            �   X                     �   Y            �   Y            �   Y            �   Y            �   Y            �   Y            �   W               �   X            �   X            �   X            �   X            �   U                    �   V            �   V            �   V            �   V            �   V            �   V            �   T               �   U            �   U            �   U            �   U            �   U            �   U            �   U            �   U            �   S                 �   T            �   T            �   T            �   T            �   T            �   T            �   T            �   Q                �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   R            �   P                  def�   Q            �   Q            �   Q            �   Q            �   Q            �   Q            �   Q            �   Q            �   Q            �   O               �   P            �   N               �   O            �   O            �   O            �   O            �   O            �   O            �   O            �   O            �   O            �   M               �   N            �   N            �   N            �   N            �   N            �   N            �   N            �   N            �   L                     �   M            �   M            �   M            �   M            �   M            �   M            �   M            �   M            �   K                    �   L            �   L            �   L            �   L            �   L            �   L            �   L            �   L            �   L            �   I                   �   J            �   J            �   J            �   J            �   J            �   J            �   H                     �   I            �   I            �   I            �   I            �   I            �   I            �   G                  �   H            �   H            �   H            �   H            �   H            �   F               �   G            �   G            �   G            �   G            �   G            �   E                �   F            �   F            �   F            �   D                �   E            �   E            �   E            �   E            �   E            �   E            �   E            �   C                 �   D            �   B               �   C            �   C            �   C            �   A                �   B            �   B            �   B            �   @                  �   A            �   A            �   A            �   ?                �   @            �   @            �   >               �   ?            �   ?            �   =                  def�   >            �   >            �   <               �   =            �   =            �   =            �   =            �   =            �   =            �   :                      return word_logits5��    :                    �              	       �    ;                     �                    �    ;                      �                     �    ;                     �                     �    <                     �                    �    <                    �                     �    =                     �                     �    =                     �                     �    >                      �                     �    >                    �                     �    ?                     �                     �    ?   
                                      �    @                                          �    @                                         �    A                     $                     �    A                     3                     �    B                      :                     �    B                    J                     �    C                    Q                     �    D                  )   W              )       �    D   +                 �                     �    E                     �                     �    E                    �                     �    F                     �                     �    F                    �                     �    G                     �                     �    G   "                 �                     �    H                  %   �              %       �    H   ,                 	                     �    I                  %   	              %       �    I   *                 ;	                     �    K                  :   C	              :       �    K   @                 }	                     �    L                  3   �	              3       �    L   :                  �	                     �    M                   ;   �	              ;       �    M   ;                 �	                     �    N                  ;   
              ;       �    N   <                  <
                     �    O                     C
                     �    P                  9   K
              9       �    P   @                 �
                     �    Q                  a   �
              a       �    Q   c                 �
                     �    S                  ,   �
              ,       �    S   /                                      �    T                  /   #              /       �    T   0                 R                     �    U                  %   Y              %       �    U   +                 ~                     �    W                     �                     �    W                    �                     �    X                  2   �              2       �    X   9                  �                     �    Y                      �                     �    Z                      �                     �    Z                    �                     �    [                  V                 V       �    [   [                 Y                     �    \                  ,   a              ,       �    \   .                 �                     �    ^                  ;   �              ;       �    ^   <                 �                     �    _                  c   �              c       �    _   g                 N                     �    `                  +   V              +       �    `   /                 �                     �    a                  3   �              3       �    a   4                 �                     �    b                  e   �              e       �    b   g                 '                     �    d                     .                     �    d                     L                     �    e                      R                     �    e                     a                     �    f                   4   h              4       �    f   4                 �                     �    g                  Q   �              Q       �    g   T                 �                     �    h                  .   �              .       �    h   0                 *                     �    i                  W   1              W       �    i   Y                 �                     �    j                     �                     �    j   "                 �                     �    l                     �                     �    l                     �                     �    m                   =   �              =       �    m   =                                      �    o                                          �    o                    %                     �    p                  4   -              4       �    p   8                 a                     �    q                  J   h              J       �    q   O                 �                     �    r                  -   �              -       �    r   /                 �                     �    s                  C   �              C       �    s   G                 0                     �    t                  $   7              $       �    t   *                  [                     �    u                     b                     �    v                     j                     5�_�                   '       ����                                                                                                                                                                                                                                                                                                                                                             el:x     �   &   (   ;      [        self.embeddings = nn.Embedding(vocab_size, embedding_size, padding_idx=padding_idx)5��    &                                        �    &                 
                
       5�_�                     )       ����                                                                                                                                                                                                                                                                                                                                                             el:�     �   )   *   ;              �   )   +   <       �   (   +   <      U        self.RNN = nn.GRU(embedding_size, hidden_size, num_layers, batch_first=True)/5��    )                      �              	       �    )                      �                     �    (   T                  �                     �    (   T                  �                     �    (   U                  �                     5��