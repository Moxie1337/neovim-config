Vim�UnDo� �%$*���D:1��a/�z� :(��g��(��   >           O                       e}�^    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e}��     �   3               �   4            �                  �               �                  �               �                  �               �                  �               �                  �               �                  �               �                  �               �                  �               �                  �               �                  �               �   
               �               �   	               �   
            �                  �   	            �                  �               �                  �               �                  �               �                  �               �                  �               �                   �               5��                                                  �                                                �                          9                      �                          ?                      �                          T                      �                          \               m       �                          �               ;       �    	                                    :       �    
                      >                      �                          ^              -       �                          �                     �                          �              A       �                          �                     �                          �                     �                          �              *       �                                               �                          6              $       �                          Z              #       �                          }                    �    3                     �                    5�_�                    I       ����                                                                                                                                                                                                                                                                                                                                                             e}��    �          ;      #define define_list(type) \   \   R    struct _list_##type;                                                         \�         ;          struct _list_##type; \       \   R    typedef struct {                                                             \�         <          typedef struct \   C    {                                                             \�         <          { \   T        int (*is_empty)(const struct _list_##type *);                              \�         <      S        int (*is_empty)(const struct _list_##type*);                              \�      	   <      6        int (*is_empty)(const struct _list_##type*); \   T        size_t (*size)(const struct _list_##type *);                               \�      	   <      S        size_t (*size)(const struct _list_##type*);                               \�      
   <      5        size_t (*size)(const struct _list_##type*); \   T        const type (*front)(const struct _list_##type *);                          \�      
   <      S        const type (*front)(const struct _list_##type*);                          \�         <      :        const type (*front)(const struct _list_##type*); \   T        void (*push_front)(struct _list_##type *, type);                           \�   	      <      S        void (*push_front)(struct _list_##type*, type);                           \�   	      <      9        void (*push_front)(struct _list_##type*, type); \   R    } _list_functions_##type;                                                    \�   
      <          } _list_functions_##type; \       \   R    typedef struct _list_elem_##type {                                           \�         =      &    typedef struct _list_elem_##type \   1    {                                           \�         =          { \   T        type _data;                                                                \�         =              type _data; \   T        struct _list_elem_##type *_next;                                           \�         =      T        struct _list_elem_##type* _next;                                           \�         =      *        struct _list_elem_##type* _next; \   R    } list_elem_##type;                                                          \�         =          } list_elem_##type; \       \   R    typedef struct _list_##type {                                                \�         >      !    typedef struct _list_##type \   6    {                                                \�         >          { \   T        size_t _size;                                                              \�         >              size_t _size; \   T        list_elem_##type *_first;                                                  \�         >      T        list_elem_##type* _first;                                                  \�         >      #        list_elem_##type* _first; \   T        list_elem_##type *_last;                                                   \�         >      T        list_elem_##type* _last;                                                   \�         >      "        list_elem_##type* _last; \   T        _list_functions_##type *_functions;                                        \�         >      T        _list_functions_##type* _functions;                                        \�         >      -        _list_functions_##type* _functions; \   R    } List_##type;                                                               \�         >          } List_##type; \       \   R    List_##type *new_list_##type();                                              \�         >      R    List_##type* new_list_##type();                                              \�         >      %    List_##type* new_list_##type(); \   R    bool list_is_empty_##type(const List_##type *list);                          \�         >      R    bool list_is_empty_##type(const List_##type* list);                          \�         >      9    bool list_is_empty_##type(const List_##type* list); \   R    size_t list_size_##type(const List_##type *list);                            \�         >      R    size_t list_size_##type(const List_##type* list);                            \�         >      7    size_t list_size_##type(const List_##type* list); \   R    const type list_front_##type(const List_##type *list);                       \�         >      R    const type list_front_##type(const List_##type* list);                       \�          >      <    const type list_front_##type(const List_##type* list); \   R    void list_push_front_##type(List_##type *list, type elem);                   \�          >      R    void list_push_front_##type(List_##type* list, type elem);                   \�      "   >      @    void list_push_front_##type(List_##type* list, type elem); \       \   R    bool list_is_empty_##type(const List_##type *list) {                         \�       "   >      R    bool list_is_empty_##type(const List_##type* list) {                         \�       "   ?      8    bool list_is_empty_##type(const List_##type* list) \       {                         \�   !   $   ?          { \   T        return list->_size == 0;                                                   \�   "   %   ?      "        return list->_size == 0; \   R    }                                                                            \�   #   '   ?          } \       \   R    size_t list_size_##type(const List_##type *list) { return list->_size; }     \�   %   '   ?      R    size_t list_size_##type(const List_##type* list) { return list->_size; }     \�   %   '   @      6    size_t list_size_##type(const List_##type* list) \   !    { return list->_size; }     \�   &   (   A          { \   #        return list->_size; }     \�   '   )   B              return list->_size; \       }     \�   (   ,   B          } \       \   R    const type list_front_##type(const List_##type *list) {                      \�   *   ,   B      R    const type list_front_##type(const List_##type* list) {                      \�   *   ,   C      ;    const type list_front_##type(const List_##type* list) \       {                      \�   +   .   C          { \   T        return list->_first->_data;                                                \�   ,   /   C      %        return list->_first->_data; \   R    }                                                                            \�   -   1   C          } \       \   R    void list_push_front_##type(List_##type *list, type elem){...}               \�   /   1   C      R    void list_push_front_##type(List_##type* list, type elem){...}               \�   /   1   D      ?    void list_push_front_##type(List_##type* list, type elem) \       {...}               \�   0   2   E          { \           ...}               \�   1   3   F              ... \       }               \�   2   6   F          } \       \   R    _list_functions_##type _list_funcs_##type = {                                \�   4   7   F      3    _list_functions_##type _list_funcs_##type = { \   R        &list_is_empty_##type,                                                   \�   5   8   F               &list_is_empty_##type, \   R        &list_size_##type,                                                       \�   6   9   F              &list_size_##type, \   R        &list_front_##type,                                                      \�   7   :   F              &list_front_##type, \   R        &list_push_front_##type,                                                 \�   8   ;   F      "        &list_push_front_##type, \   R    };                                                                           \�   9   =   F          }; \       \   R    List_##type *new_list_##type() {                                             \�   ;   =   F      R    List_##type* new_list_##type() {                                             \�   ;   =   G      $    List_##type* new_list_##type() \   3    {                                             \�   <   ?   G          { \   T        List_##type *res = (List_##type *)malloc(sizeof(List_##type));             \�   =   ?   G      T        List_##type* res = (List_##type*) malloc(sizeof(List_##type));             \�   =   @   G      H        List_##type* res = (List_##type*) malloc(sizeof(List_##type)); \   T        res->_size = 0;                                                            \�   >   A   G              res->_size = 0; \   T        res->_first = NULL;                                                        \�   ?   B   G              res->_first = NULL; \   T        res->_functions = &_list_funcs_##type;                                     \�   @   C   G      0        res->_functions = &_list_funcs_##type; \   T        return res;                                                                \�   A   D   G              return res; \       }�   D   F   H      #define List(type) \       List_##type�   G              #define new_list(type) \       new_list_##type()5��    G                   �                    �    D                   k                    �    A                  O             D       �    @   .               9             +       �    ?                               >       �    >                  �             B       �    =   F               �                    �    =   )                  �                     �    =   '                  �                     �    =                     �                     �    =                     �                     �    <                  �             3       �    ;   "                                    �    ;                     m                     �    ;                     l                     �    9                  T             �       �    8                   K             5       �    7                  (             >       �    6                  
             ?       �    5                  �             ;       �    4   1               �             (       �    2                  �             d       �    1                    �                     �    0                    |                     �    /   =                 t                     �    /   ,                  c                     �    /   +                  b                     �    -                  .             �       �    ,   #               &             4       �    +                                       �    *   9                �                    �    *   3                  �                     �    *   2                  �                     �    (                  �             Z       �    '                   �                    �    &                   �                    �    %   4                �                    �    %   .                  �                     �    %   -                  �                     �    #                  K             �       �    "                   C             7       �    !                                       �        6                                    �        0                                       �        /                                       �       >               �             h       �       ,                  �                     �       +                  �                     �       :               �                    �       3                  �                     �       2                  �                     �       5               [                     �       .                  T                     �       -                  S                     �       7               #                    �       0                                       �       /                                       �       #               �             2       �                         �                     �                         �                     �                      �             �       �       +               �             ,       �                         �                     �                         �                     �                       z             9       �                         s                     �                         r                     �       !               W             8       �                         O                     �                         N                     �                      3             D       �                                   6       �                                           �                      �             �       �       (               �             /       �       !                  �                     �                          �                     �                      �             F       �                      �             1       �       $                �                    �    
                  [             �       �    	   7               ;                    �    	   .                  2                     �       8                                    �       5                  �                      �       3               �              %       �       0                  �                      �       4               �              $       �       1                  �                      �                      Y              C       �                       Q                     �                      6              �       �                              	       �       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e}�2     �          ;      P#define define_list(type)                                                      \5��                                                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e}�3     �          <       5��                                                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e}�4     �          =       5��                                                  �                                              5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             e}�8     �          =      
#include<>5��        	                  	                      �        	                 	                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e}�;     �          =      #include<stdio.h>5��                                                �                                                �                     	                 	       5�_�      	                 	    ����                                                                                                                                                                                                                                                                                                                                                             e}�@     �         >      
#include<>5��       	                                        �       	                                      5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             e}�C     �         >      #include<string.h>5��                         $                      �                       
   %               
       5�_�   	              
      	    ����                                                                                                                                                                                                                                                                                                                                                             e}�F     �         ?      
#include<>5��       	                  .                      �       	                 .                     5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             e}�J    �          ?      #include<stdio.h>   #include<string.h>   #include<stdlib.h>5��                                7       :       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e}��     �         ?       5��                          ;                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e}��     �         @       5��                       
   ;               
       5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             e}��     �         @      
#include<>5��       	                  D                      �       	              	   D              	       �       	       	       	   D       	       	       �       	       	          D       	              �       	              
   D              
       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e}��    �          @      #include <stdio.h>   #include <stdlib.h>   #include <string.h>   #include<stdbool.h>5��                                N       O       5�_�                    -       ����                                                                                                                                                                                                                                                                                                                                                             e}�S     �   ,   .   @      P  void list_push_front_##type(List_##type *list, type elem){...}               \5��    ,                     �                     5�_�                    -        ����                                                                                                                                                                                                                                                                                                                            -          -          V       e}�U     �   ,   -          Q  Vvoid list_push_front_##type(List_##type *list, type elem){...}               \5��    ,                      �      R               5�_�                    -   O    ����                                                                                                                                                                                                                                                                                                                            -          -          V       e}�V     �   ,   .   ?      P                                                                               \5��    ,   <                 �                    5�_�                     -        ����                                                                                                                                                                                                                                                                                                                            -   =       -   =       V   =    e}�]    �   ,   -          ?                                                            vx\5��    ,                      �      @               5��