Vim�UnDo� �,��@��hlC�P	�m��5;����2�                 #   #       #   #   #    ei�k    _�                  #           ����                                                                                                                                                                                                                                                                                                                                                v       ei�j    �                  �                  return {   	"tomtom/tcomment_vim",   	event = "BufRead",   	config = function()   		vim.g.tcomment_maps = true   .		vim.g.tcomment_textobject_inlinecomment = ''       		vim.cmd([[   nmap <LEADER>cn g>c   vmap <LEADER>cn g>   nmap <LEADER>cu g<c   vmap <LEADER>cu g<   unmap ic   		]])   	end   }5��                                             �                                               5�_�              #              ����                                                                                                                                                                                                                                                                                                                                                             ei�     �                5��                          �                      �                          �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ei�     �             �               !	local filetype = vim.bo.filetype   -	if filetype == "cpp" or filetype == "c" then   	5��                         �               Q       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ei�
     �                   !	local filetype = vim.bo.filetype5��                         �                     �                          �                      �                         �                      5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ei�    �   	             5��    	                      �                      5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             ei�k     �               	   	end5��                        S                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ei�l     �               	end5��                         S                     �                        S                    �                        S                    5�_�         	                 ����                                                                                                                                                                                                                                                                                                                                                             eiЋ     �   
            					vim.cmd([[5��    
                     �                      �    
                    �                     �    
                    �                     �    
                    �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eiЎ     �               						nmap <LEADER>cn g>c5��                          �                      �                         �                     �                        �                     �                        �                     �                        �                     �                        �                     �                        �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eiА     �               						vmap <LEADER>cn g>5��                                               �                                             �                                            �                                            �                                            �                                            �                                            �                                            �                                              5�_�                           ����                                                                                                                                                                    ,                                                                                                                                                                           v       eiй     �               						nmap <LEADER>cu g<c5��                          -                     �                         -                    �                        .                    �                        /                    �                        0                    �                        1                    �                        2                    5�_�                            ����                                                                                                                                                                    ,                                                                                                                                                                           v       eiм     �               						vmap <LEADER>cu g<5��                          H                     �                         H                    �                        I                    �                        J                    �                        K                    �                        L                    �                        M                    �                        N                    �                         N                     5�_�                            ����                                                                                                                                                                    ,                                                                                                                                                                           v       eiп     �               						unmap ic5��                          a                     �                         a                    �                        b                    �                        c                    �                        d                    �                        e                    �                        f                    5�_�                    
        ����                                                                                                                                                                    ,                                                                                                                                                                            v       ei��     �   	             �               -	if filetype == "cpp" or filetype == "c" then5��       -                  �                      5�_�                           ����                                                                                                                                                                    ,                                                                                                                                                                            v       ei��    �                 return {   	"tomtom/tcomment_vim",   	event = "BufRead",   	config = function()   		vim.g.tcomment_maps = true   .		vim.g.tcomment_textobject_inlinecomment = ''       "		local filetype = vim.bo.filetype   .		if filetype == "cpp" or filetype == "c" then   			vim.cmd([[   						nmap <LEADER>cn g>c   						vmap <LEADER>cn g>   						nmap <LEADER>cu g<c   						vmap <LEADER>cu g<   						unmap ic   		]])   		end   	end   }    �              5��                                 }            �                                               5�_�                          ����                                                                                                                                                                                                                                                                                                                                                 v       ei��     �   
            				nmap <LEADER>cn g>c5��    
                     �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 v       ei�     �               				vmap <LEADER>cn g>5��                                              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 v       ei�     �               				nmap <LEADER>cu g<c5��                         *                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 v       ei�     �               				vmap <LEADER>cu g<5��                         B                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 v       ei�     �               				unmap ic5��                         Y                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 v       ei�.     �   
            				nmap <LEADER>cn g#c5��    
                                        5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 v       ei�3     �               				vmap <LEADER>cn g#5��                        $                    5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                 v       ei�8     �               				nmap <LEADER>cu g//c5��                        ;                    5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                 v       ei�>     �               				vmap <LEADER>cu g//5��                        T                    �                         V                     5�_�   !               "          ����                                                                                                                                                                                                                                                                                                                                                             ei�C    �                 return {   	"tomtom/tcomment_vim",   	event = "BufRead",   	config = function()   		vim.g.tcomment_maps = true   .		vim.g.tcomment_textobject_inlinecomment = ''       "		local filetype = vim.bo.filetype   .		if filetype == "cpp" or filetype == "c" then   			vim.cmd([[   				nmap <LEADER>cn g#c   				vmap <LEADER>cn g#   				nmap <LEADER>cu g//c   				vmap <LEADER>cu g//   				unmap ic   		]])   		end   	end   }    �              5��                                 v      w      �                          w                     5�_�                           ����                                                                                                                                                                                                                                                                                                                            
                    v       ei��     �   
            					nmap <LEADER>cn g>c�   	            %			vim.cmd([[					nmap <LEADER>cn g>c5��    
                      �                      �    	                     �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eiД     �               						nmap <LEADER>cu g<c5��                          -                     �                         -                    �                        .                    �                        /                    �                        0                    �                        1                    �                        2                    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eiЖ     �               						vmap <LEADER>cu g<5��                          H                     �                         H                    �                        I                    �                        J                    �                        K                    �                        L                    �                        M                    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eiЙ     �               						unmap ic5��                          b                     �                         b                    �                        c                    �                        d                    �                        e                    �                        f                    �                        g                    5�_�                     
        ����                                                                                                                                                                	   ,                                                                                                                                                                                        eiТ     �   	             �               -	if filetype == "cpp" or filetype == "c" then5��       -                  �                      5�_�      
          	          ����                                                                                                                                                                                                                                                                                                                                                             ei�p     �               	end5��                         S                     �                         R                    �                        S                    �                        S                    5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             ei�v     �               	5��                         S                     �                         R                    �                         S                     5�_�   
                          ����                                                                                                                                                                                                                                                                                                                                                             ei�{    �               	end	5��                          R                     �                         R                    5�_�                           ����                                                                                                                                                                                                                                                                                                                            
                      V        ei�<     �   
           �   	             5��    
                      �       o               �    	                      �                      �    	                      �                      5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             ei�     �   	             �               -	if filetype == "cpp" or filetype == "c" then5��       -                  �                      5��